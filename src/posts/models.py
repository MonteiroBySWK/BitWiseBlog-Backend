class PostModel:
    title: str
    author: str
    contain: str
    likes: int
    dislikes: int

    def __init__(self, title, author, contain, likes=0, dislikes=0) -> None:
        self.title = title
        self.author = author
        self.contain = contain
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self) -> str:
        return f"Post by {self.author}"
