import random


class University:
    def __init__(self, name: str, founding_year: int, country: str, ranking: int, total_students: int) -> None:
        self.name = name
        self.founding_year = founding_year
        self.country = country
        self.ranking = ranking
        self.total_students = total_students

    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country, self.ranking, self.total_students))

    def get_age(self, current_year: int) -> int:
        return current_year - self.founding_year

    def display_info(self) -> None:
        print(f"University: {self.name}")
        print(f"Founded: {self.founding_year} ({self.get_age(2023)} years old)")
        print(f"Country: {self.country}")
        print(f"Ranking: {self.ranking}")
        print(f"Total Students: {self.total_students}")
        print("=" * 30)


if __name__ == "__main__":
    tmp_list = list(range(1000))
    random.shuffle(tmp_list)
    # Play around with sort and sorted
    sorted_tmp = sorted(tmp_list)
    print("Sorted List:", sorted_tmp)
    # Using sort in-place
    tmp_list.sort()
    print("Original List after sort:", tmp_list)
    # Create University objects with additional properties
    universities_objects = [
        University("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany", 300, 15000),
        University("Harvard University", 1636, "USA", 1, 22000),
        University("Technische Universität München", 1868, "Germany", 150, 18000),
        University("RWTH Aachen", 1870, "Germany", 200, 16000)
    ]

    # Sort university_objects by age
    universities_objects_by_age = sorted(universities_objects, key=lambda x: x.founding_year)

    # Sort university_objects by name
    universities_objects_by_name = sorted(universities_objects, key=lambda x: x.name)

    # Print the results
    print("University Objects by Age:")
    for university in universities_objects_by_age:
        university.display_info()

    print("University Objects by Name:")
    for university in universities_objects_by_name:
        university.display_info()
