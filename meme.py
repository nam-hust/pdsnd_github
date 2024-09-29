import os
import random

# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""

    # Select a random image if no path is provided
    if path is None:
        images_dir = "./_data/photos/dog/"
        imgs = [os.path.join(root, name)
                for root, _, files in os.walk(images_dir)
                for name in files if name.endswith(('jpg', 'png', 'jpeg'))]

        img = random.choice(imgs)
    else:
        img = path[0]

    # Select a random quote if no body is provided
    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]

        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if not author:
            raise ValueError("Author is required when a quote body is provided.")
        quote = QuoteModel(body, author)

    # Generate the meme
    meme_generator = MemeEngine('./tmp')
    meme_path = meme_generator.make_meme(img, quote.body, quote.author)

    return meme_path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args = None
    print(generate_meme(args.path, args.body, args.author))
