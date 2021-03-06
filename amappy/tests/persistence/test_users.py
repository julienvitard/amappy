#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestUsersMemoryDB(unittest.TestCase):

    def setUp(self):
        from amappy.persistence.users import UsersMemoryDB
        UsersMemoryDB.reset()

    def test_init_db(self):
        from amappy.persistence.users import UsersMemoryDB
        self.assertEqual(UsersMemoryDB.USERS_BY_ID, {})
        self.assertEqual(UsersMemoryDB.USERS_BY_NAME, {})

    def test_get_id(self):
        from amappy.persistence.users import UsersMemoryDB
        self.assertEqual(UsersMemoryDB.get_id(), 1)

        UsersMemoryDB.USERS_BY_ID = {2: ""}
        self.assertEqual(UsersMemoryDB.get_id(), 3)

        UsersMemoryDB.USERS_BY_ID = {2: "", 5: ""}
        self.assertEqual(UsersMemoryDB.get_id(), 6)

    def test_create(self):
        from amappy.persistence.users import UsersMemoryDB
        data = {
            "name": "Doe",
        }
        identifier = UsersMemoryDB.create(data=data)
        self.assertIsNotNone(identifier)
        self.assertEqual(identifier, 1)
        self.assertEqual(len(UsersMemoryDB.USERS_BY_ID.keys()), 1)
        self.assertEqual(len(UsersMemoryDB.USERS_BY_NAME.keys()), 1)

    def test_create_value_error(self):
        from amappy.persistence.users import UsersMemoryDB
        data = {"name": "Doe"}
        UsersMemoryDB.create(data=data)

        with self.assertRaises(ValueError):
            new_data = {"name": "Doe"}
            UsersMemoryDB.create(data=new_data)

    def test_read_by_name(self):
        from amappy.persistence.users import UsersMemoryDB
        data = {
            "name": "Doe",
        }
        identifier = UsersMemoryDB.create(data=data)
        self.assertIsNotNone(identifier)
        self.assertEqual(identifier, 1)
        user = UsersMemoryDB.read(name="Doe")
        self.assertEqual(user["name"], "Doe")
        self.assertEqual(user["id"], 1)

    def test_read_by_id(self):
        from amappy.persistence.users import UsersMemoryDB
        data = {
            "name": "Doe",
        }
        identifier = UsersMemoryDB.create(data=data)
        self.assertIsNotNone(identifier)
        self.assertEqual(identifier, 1)
        user = UsersMemoryDB.read(id=1)
        self.assertEqual(user["name"], "Doe")
        self.assertEqual(user["id"], 1)
