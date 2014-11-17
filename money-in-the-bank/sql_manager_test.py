import sys
import unittest

sys.path.append("..")

import sql_manager
import hashlib


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123123')

        sql_manager.cursor.execute('''SELECT Count(*)  FROM clients WHERE username = (?)
                                     AND password = (?)''', ('Dinko', '123123'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_injection(self):
        logged_user = sql_manager.login(' \' OR 1 = 1 --', '123')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_strong_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "abCd4567@"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_weak_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        self.assertEqual(sql_manager.change_pass(new_password, logged_user), None)

    def test_hashing(self):
        hash_object = hashlib.sha1(b'123123')
        hex_dig = hash_object.hexdigest()
        sql_manager.register('Dinko', hex_dig)
        logged_user = sql_manager.login('Dinko', hex_dig)
        self.assertEqual(logged_user.get_username(), 'Dinko')

    def test_balance(self):
        self.assertEqual(sql_manager.balance('Tester'), 'your balance is 0.0')
        sql_manager.register('Dinko', '123123')
        sql_manager.deposit('Dinko', 100)
        self.assertEqual(sql_manager.balance('Dinko'), 'your balance is 100.0')

    def test_deposit(self):
        sql_manager.deposit('Tester', 200)
        self.assertEqual(sql_manager.balance('Tester'), 'your balance is 200.0')

    def test_withdraw(self):
        sql_manager.deposit('Tester', 200)
        sql_manager.withdraw('Tester', 50)
        self.assertEqual(sql_manager.balance('Tester'), 'your balance is 150.0')


if __name__ == '__main__':
    unittest.main()
