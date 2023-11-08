class Project:
    def __init__(self, name, description, lisence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.lisence = lisence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- " +"\n- ".join(dependencies) + "\n" if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLisence: {self.lisence or '-'}"  + "\n"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
    # Jokin muutos