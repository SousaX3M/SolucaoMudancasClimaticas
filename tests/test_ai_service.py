import os
import unittest
from unittest.mock import Mock, patch

from ai_service import GeminiServiceError, _error_for_status, analyze_country


class AnalyzeCountryTests(unittest.TestCase):
    def test_requires_api_key(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(GeminiServiceError, "GEMINI_API_KEY"):
                analyze_country("Brasil")

    def test_depleted_credits_have_actionable_message(self):
        error = _error_for_status(402)

        self.assertIn("sem créditos", str(error))
        self.assertEqual(error.status_code, 503)

    @patch.dict(
        os.environ,
        {
            "GEMINI_API_KEY": "test-key",
            "GEMINI_MODEL": "gemini-4-hydrogen",
        },
    )
    @patch("ai_service.genai.Client")
    def test_returns_gemini_output(self, client_factory):
        client = Mock()
        client.interactions.create.return_value.output_text = "Análise de teste."
        client_factory.return_value.__enter__.return_value = client

        result = analyze_country("Brasil")

        self.assertEqual(result, "Análise de teste.")
        client_factory.assert_called_once_with(api_key="test-key")
        client_factory.return_value.__exit__.assert_called_once()
        request = client.interactions.create.call_args.kwargs
        self.assertEqual(request["model"], "gemini-4-hydrogen")
        self.assertIn("Brasil", request["input"])
        self.assertEqual(request["timeout"], 60)


if __name__ == "__main__":
    unittest.main()
