class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        report = ""
        for key, value in self.data.items():
            report += f"{key}: {value}\n"
        return report

    def generate_table_report(self):
        report = ""
        for key, value in self.data.items():
            report += f"| {key} | {value} |\n"
        return report

    def generate_csv_report(self):
        report = ""
        for key, value in self.data.items():
            report += f"{key},{value}\n"
        return report


data = {
    "Name": "John Doe",
    "Age": 30,
    "City": "New York"
}

generator = ReportGenerator(data)

print("Text Report:")
print(generator.generate_report())

print("\nTable Report:")
print(generator.generate_table_report())

print("\nCSV Report:")
print(generator.generate_csv_report())
```

Kodda quyidagi funksiyalar mavjud:

- `generate_report`: Matn formatida hisobotni yaratadi.
- `generate_table_report`: Jadvallar formatida hisobotni yaratadi.
- `generate_csv_report`: CSV formatida hisobotni yaratadi.

Hisobot yaratish uchun `ReportGenerator` klassi yaratiladi va unda ma'lumotlar saqlanadi. Keyin `generate_report`, `generate_table_report` yoki `generate_csv_report` funksiyalari orqali hisobot yaratiladi.
