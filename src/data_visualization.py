```python
import matplotlib.pyplot as plt
import pandas as pd

def visualizeData(platformData):
    # Convert platformData to DataFrame for easier manipulation
    df = pd.DataFrame(platformData)

    # AI agent creation visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['ai_agent_creation'], color='blue')
    plt.title('AI Agent Creation Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of AI Agents Created')
    plt.show()

    # Transaction volume visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['transaction_volume'], color='green')
    plt.title('Transaction Volume Over Time')
    plt.xlabel('Time')
    plt.ylabel('Transaction Volume')
    plt.show()

    # Token exchanges visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['token_exchanges'], color='red')
    plt.title('Token Exchanges Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Token Exchanges')
    plt.show()
```