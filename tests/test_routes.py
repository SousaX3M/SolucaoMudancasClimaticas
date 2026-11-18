import unittest
from unittest.mock import patch

import main
from ai_service import GeminiServiceError


class AnalysisRouteTests(unittest.TestCase):
    def setUp(self):
        main.app.config.update(TESTING=True)
        self.client = main.app.test_client()

    @patch("main.generate_country_analysis", return_value="Análise gerada.")
    def test_analyze_country_renders_analysis(self, generate_analysis):
        response = self.client.post("/analisar", data={"country": "Brasil"})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"An\xc3\xa1lise gerada.", response.data)
        self.assertIn(b"Conte\xc3\xbado gerado por IA.", response.data)
        generate_analysis.assert_called_once_with("Brasil")

    @patch("main.generate_country_analysis", return_value="<script>alert(1)</script>")
    def test_analysis_is_escaped_in_html(self, _generate_analysis):
        response = self.client.post("/analisar", data={"country": "Brasil"})

        self.assertIn(b"&lt;script&gt;alert(1)&lt;/script&gt;", response.data)
        self.assertNotIn(b"<script>alert(1)</script>", response.data)

    @patch("main.random.choice", return_value="Jap\xc3\xa3o")
    @patch("main.generate_country_analysis", return_value="Análise aleatória.")
    def test_random_country_also_generates_analysis(
        self,
        generate_analysis,
        _random_choice,
    ):
        response = self.client.post("/pais-aleatorio")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"An\xc3\xa1lise aleat\xc3\xb3ria.", response.data)
        generate_analysis.assert_called_once_with("Jap\xc3\xa3o")

    @patch(
        "main.generate_country_analysis",
        side_effect=GeminiServiceError("Confira a chave.", status_code=503),
    )
    def test_service_error_is_shown_to_user(self, _generate_analysis):
        response = self.client.post("/analisar", data={"country": "Brasil"})

        self.assertEqual(response.status_code, 503)
        self.assertIn(b"Confira a chave.", response.data)


if __name__ == "__main__":
    unittest.main()
