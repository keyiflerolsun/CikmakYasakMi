class History:
    def __init__(self):
        self.hist: dict = {}

    def add_user(self, uid: int) -> None:
        self.hist.update({uid: {"query": []}})

    def add_data(self, uid: int, data: str) -> None:
        self.hist[uid]["query"].append(data)

    def show_history(self, uid: int) -> None:
        print(f"UserID: {uid} - Query: {self.hist[uid]['query']}")

    def go_back(self, uid: int) -> None:
        self.hist[uid]["query"] = self.hist[uid]["query"][0:-2]

    def get_data(self, uid: int) -> list:
        return [self.hist[uid]["query"][0], self.hist[uid]["query"][1]]

    def print_data(self) -> None:
        print(self.hist)
