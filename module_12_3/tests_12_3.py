import unittest
import suite_12_3 as ST


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_walk(self):
        runner = ST.Runner("Ivan")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_run(self):
        runner = ST.Runner("Igor")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_challenge(self):
        runner1 = ST.Runner("Alex")
        runner2 = ST.Runner("Kirill")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = ST.Runner("Усэйн", 10)
        self.andrey = ST.Runner("Андрей", 9)
        self.nick = ST.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            print(results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_race_usein_and_nick(self):
        tournament = ST.Tournament(90, self.usein, self.nick)
        results = tournament.start()
        self.__class__.all_results['race_1'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_race_andrey_and_nick(self):
        tournament = ST.Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results['race_2'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены ")
    def test_race_usein_andrey_and_nick(self):
        tournament = ST.Tournament(90, self.usein, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results['race_3'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")


Suite_ST = unittest.TestSuite()
Suite_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
Suite_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(Suite_ST)
