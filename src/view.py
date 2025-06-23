def printTable(table: list[list[str]]):
    for i in table:
        for j in i:
            print(j, end="  ")
        print()