import os

from google import genai
from google.genai._interactions_errors import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
)


DEFAULT_MODEL = "gemini-4-hydrogen"
REQUEST_TIMEOUT_SECONDS = 60


class GeminiServiceError(Exception):
    def __init__(self, message, status_code=503):
        super().__init__(message)
        self.status_code = status_code


def _prompt_for_country(country):
    return f"""Prepare uma análise educativa em português brasileiro sobre o país informado: {country}

Organize a resposta com estes títulos em texto simples, sem Markdown:
1. Problemas ambientais
2. Impactos das mudanças climáticas
3. Causas e áreas afetadas
4. Consequências para a população
5. Possíveis ações e soluções

Distinga problemas ambientais gerais daqueles ligados às mudanças climáticas.
Use linguagem clara e concisa, sem tabelas, asteriscos ou símbolos de título.
Não invente estatísticas, notícias, datas, fontes ou links. Se não tiver
segurança sobre um detalhe específico do país, declare essa limitação. Você
não recebeu fontes nem dados atuais; não apresente a resposta como notícia
recente ou informação verificada."""


def _error_for_status(status_code):
    if status_code == 402:
        return GeminiServiceError(
            "O projeto Google associado à chave está sem créditos ou não está "
            "no nível gratuito. Confira o projeto e o faturamento no AI Studio."
        )
    if status_code == 429:
        return GeminiServiceError(
            "O limite de uso do Gemini foi atingido. Aguarde a renovação da cota "
            "e tente novamente.",
            status_code=429,
        )
    if status_code in (401, 403):
        return GeminiServiceError(
            "A chave da API Gemini é inválida ou não tem acesso a este projeto."
        )
    if status_code == 404:
        return GeminiServiceError(
            "O modelo Gemini configurado não foi encontrado. Confira GEMINI_MODEL."
        )
    return GeminiServiceError(
        f"A API Gemini retornou um erro HTTP {status_code}. Tente novamente mais tarde."
    )


def analyze_country(country):
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise GeminiServiceError(
            "A chave do Gemini não está configurada. Defina GEMINI_API_KEY "
            "no ambiente e reinicie a aplicação."
        )

    model = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    try:
        with genai.Client(api_key=api_key) as client:
            interaction = client.interactions.create(
                model=model,
                input=_prompt_for_country(country),
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
    except APIStatusError as error:
        raise _error_for_status(error.status_code) from error
    except (APIConnectionError, APITimeoutError) as error:
        raise GeminiServiceError(
            "Não foi possível conectar à API Gemini. Verifique a conexão e tente novamente."
        ) from error
    except APIResponseValidationError as error:
        raise GeminiServiceError(
            "A API Gemini retornou uma resposta inesperada. Tente novamente mais tarde."
        ) from error
    except APIError as error:
        raise GeminiServiceError(
            "A solicitação à API Gemini falhou. Tente novamente mais tarde."
        ) from error

    analysis = interaction.output_text
    if not isinstance(analysis, str) or not analysis.strip():
        raise GeminiServiceError(
            "O Gemini não retornou uma análise. Tente novamente."
        )

    return analysis.strip()
