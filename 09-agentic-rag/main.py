from dotenv import load_dotenv

load_dotenv()

from graph.graph import app


def main() -> None:
    print("Hello Advanced REG")
    print(app.invoke(input={"question": "What is agent memory"}))  # type: ignore


if __name__ == "__main__":
    main()
