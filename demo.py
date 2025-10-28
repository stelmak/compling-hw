from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()

    sample_text = "Егор Крид — российский певец, рэпер, автор песен, актёр, ютубер, стример и телеведущий. Сольную карьеру начал в 2011 году под псевдонимом KReeD, сейчас выступает под именем Егор Крид. Является автором и исполнителем собственных песен. Заслуженный артист Республики Башкортостан!"

    results = tokenizer.tokenize_all(sample_text)

    for method, tokens in results.items():
        print(f"{method}: {tokens}")
        print('-'*10)

if __name__ == "__main__":
    main()
    pass
