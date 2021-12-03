###############################################################################
# Copyright (C) 2021, created on December 03, 2021
# Written by Justin Ho
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# This source code is distributed in the hope that it will be useful and
# without warranty or implied warranty of merchantability or fitness for a
# particular purpose.
###############################################################################

import bcrypt
from sqlalchemy.sql import select


class UserMixin:

    def authenticate(self, session, email, password):
        """authenticates a user

        Parameters
        ----------
        session : session
            database session
        email : str
            email string of user
        password : str
            password string of user

        Returns
        -------
        bool
            returns True if user is authenticated, False otherwise
        """
        query = select(self.password).filter(self.email == email)
        pw = session.execute(query).scalar()
        if pw:
            return bcrypt.checkpw(password.encode('utf-8'), pw)
        else:
            return False
