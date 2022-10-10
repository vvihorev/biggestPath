import re


def biggestPath(X: dict) -> str:
    def bP(cur: dict | list, pwd: str) -> str:
        if len(pwd) > 255 or re.search(r"[^0-9a-zA-Z/]", pwd) is not None:
            return "/"
        # if cur is a list
        if type(cur) == list:
            files = [file for file in cur if re.search(r"[^0-9a-zA-Z/]", file) is None]
            if len(files) == 0 or len(set(cur)) < len(cur):
                return "/"
            file = min(files, key=(lambda file: len(file)))
            if len(pwd + file) > 255:
                return "/"
            return pwd + "/" + file
        # if cur is a dict
        if cur == {}:
            return pwd
        if len(set(cur.keys())) < len(cur.keys()):
            return "/"
        return max(
            [bP(contents, pwd + "/" + subdir) for subdir, contents in cur.items()],
            key=(lambda x: len(x.split("/"))),
        )
    return bP(X, "")
