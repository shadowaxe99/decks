```python
import unittest
from src.personalization_system import adjustAICharacter

class TestPersonalizationSystem(unittest.TestCase):

    def setUp(self):
        self.aiCharacter = {
            "name": "AI Agent",
            "personality_traits": ["friendly", "knowledgeable"],
            "conversation_history": []
        }
        self.investorPreferences = {
            "preferred_personality": "funny",
            "preferred_topics": ["blockchain", "AI"]
        }

    def test_adjustAICharacter(self):
        adjustAICharacter(self.aiCharacter, self.investorPreferences)
        self.assertIn("funny", self.aiCharacter["personality_traits"])
        self.assertIn("blockchain", self.aiCharacter["conversation_history"])
        self.assertIn("AI", self.aiCharacter["conversation_history"])

if __name__ == '__main__':
    unittest.main()
```