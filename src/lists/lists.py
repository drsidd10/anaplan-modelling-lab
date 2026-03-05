# lists.py — Anaplan-style Lists & Hierarchies

class List:
    """Represents a simple flat list (like an Anaplan list)."""
    def __init__(self, name, items):
        self.name = name
        self.items = list(items)

    def __repr__(self):
        return f"List({self.name}, {len(self.items)} items)"


class Hierarchy:
    """Represents a parent–child hierarchy (Anaplan-style)."""
    def __init__(self, name, parents, children):
        self.name = name
        self.parents = parents
        self.children = children

    def parents_of(self, item):
        return self.parents.get(item, None)

    def children_of(self, item):
        return [k for k, v in self.parents.items() if v == item]

    def __repr__(self):
        return f"Hierarchy({self.name})"


class ListSubset:
    """Anaplan-style list subset using Boolean masks."""
    def __init__(self, list_obj, mask):
        self.list = list_obj
        self.mask = mask

    @property
    def items(self):
        return [i for i, keep in zip(self.list.items, self.mask) if keep]

    def __repr__(self):
        return f"ListSubset({self.list.name}, {len(self.items)} items)"
