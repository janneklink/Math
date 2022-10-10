
def get_ascii_dict(start:int, end:int) -> dict:
    """start is included, end is excluded"""
    ascii_dict = {}
    for current in range(start,end):
        ascii_dict[str(current)] = 0
    return ascii_dict


if __name__ == "__main__":
    print(get_ascii_dict(10,15))

with open("ulysses.txt","r") as file:
    lines = file.readlines()
