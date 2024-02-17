import runpy
from fastchat.model import model_adapter #import VicunaAdapter, register_model_adapter, model_adapters


class ChatMLAdapter(model_adapter.VicunaModelAdapter):

    def match(self, model_path: str):
        return 'vicuna' in model_path.lower() or super().match(model_path)


def main():
    model_adapter.model_adapters = []
    model_adapter.register_model_adapter(ChatMLAdapter)

    runpy.run_module("vllm.entrypoints.openai.api_server", {}, "__main__")


if __name__ == '__main__':
    main()
