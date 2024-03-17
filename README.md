git clone https://github.com/microsoft/TaskWeaver.git
cd TaskWeaver
# install the requirements
pip install -r requirements.txt

Before running TaskWeaver, you need to provide your LLM configurations. Taking OpenAI as an example, you can configure taskweaver_config.json file as follows.

OpenAI
{
  "llm.api_key": "the api key",
  "llm.model": "the model name, e.g., gpt-4"
}