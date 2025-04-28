class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("to_html() not implemented Error")

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode musí mít hodnotu (value).")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode nemá hodnotu (value).")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
