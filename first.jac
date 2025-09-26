def lovejac() -> str{
    return "With Jac Python becomes even more awesome.";
}

#:__main__ replaces if __name__ == "__main__": Much cleaner syntax
with entry:__main__ {
    print(f"{lovejac()}");
}