```python
import unittest
from src.ai_character_interaction import interactWithAI, aiCharacter

class TestAICharacterInteraction(unittest.TestCase):

    def setUp(self):
        self.aiCharacter = aiCharacter
        self.investorMessage = "Hello AI"

    def test_interactWithAI(self):
        response = interactWithAI(self.aiCharacter, self.investorMessage)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_aiCharacter(self):
        self.assertIsNotNone(self.aiCharacter)
        self.assertIsInstance(self.aiCharacter, dict)
        self.assertIn('personality', self.aiCharacter)
        self.assertIn('conversation_history', self.aiCharacter)

if __name__ == '__main__':
    unittest.main()
```