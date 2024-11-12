from mrjob.job import MRJob
from mrjob.step import MRStep

class NumberCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_numbers,
                   reducer=self.reducer_count_numbers)
        ]

    def mapper_get_numbers(self, _, line):
        # Každé číslo na řádku se převede na celé číslo a zapíše s hodnotou 1
        try:
            number = int(line.strip())
            yield number, 1
        except ValueError:
            pass  # Pokud na řádku není číslo, přeskakujeme

    def reducer_count_numbers(self, number, counts):
        # Sečteme všechny výskyty (1) každého čísla
        yield number, sum(counts)

if __name__ == '__main__':
    NumberCount.run()
