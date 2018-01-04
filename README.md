# Price Formatter

Converts a string in a particular format (e.g. `3245.000000`) to another particular format (e.g. `3 245`). For more examples, refer to the tests.

# Using
In order to work, requires Python 3. You can either import `format_price` function or use the CLI interface:
```bash
$ python format_price.py
Enter the price to process (e.g. "3245.0000"): 12332.013000
12 332.013
```

* As import module

        from format_price import format_price
        print(format_price('446,00'))


Run the tests: `python tests.py`.
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
