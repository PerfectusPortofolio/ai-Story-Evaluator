import click
from .evaluator import evaluate_story_structure, evaluate_creativity
from .humor_tone import analyze_tone
from .utils import save_results, load_text_file


@click.command()
@click.option("--text", help="Text to analyze")
@click.option("--file", help="Path to a text file")
@click.option("--full", is_flag=True, help="Run full analysis")
def main(text, file, full):
    if file:
        text = load_text_file(file)

    if not text:
        click.echo("Provide text or file.")
        return

    click.echo("\nRunning narrative analysis...\n")

    structure = evaluate_story_structure(text)
    results = {"structure": structure}

    if full:
        tone = analyze_tone(text)
        creativity = evaluate_creativity(text)
        results["tone"] = tone
        results["creativity"] = creativity

    click.echo("Results:\n")
    for k, v in results.items():
        click.echo(f"{k.upper()}:\n{v}\n")

    save_results(results)


if __name__ == "__main__":
    main()
