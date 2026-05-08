from processor import GradeProcessor
from input_readers import ConsoleInputReader
from output_writers import ConsoleOutputWriter


class App:
    def __init__(self, reader, writer):
        self._reader = reader
        self._writer = writer
        self._processor = GradeProcessor()

    def run(self):
        student = self._reader.read()
        processed_student = self._processor.process(student)
        self._writer.write(processed_student)


if __name__ == "__main__":
    reader = ConsoleInputReader()
    writer = ConsoleOutputWriter()

    app = App(reader, writer)
    app.run()