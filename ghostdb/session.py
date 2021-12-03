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

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

conn_template = "mysql://%(username)s:%(password)s@%(host)s:%(port)s/%(dbname)s"

sessions = {}


def get_session(username, password, host, dbname, port=3306, echo=False, pool_pre_ping=False):
    """Gets a session to the database.

    Parameters
    ----------
    username : str
        username
    password : str
        password
    host : str
        string to host
    dbname : str
        database
    port : int, optional
        port of database, by default 3306
    echo : bool, optional
        echos sql commands if true, by default False
    pool_pre_ping : bool, optional
        set true for long lived processes, by default False

    Returns
    -------
    session : sqlalchemy.orm.session.Session
        return session to database
    """
    auth_info = {"username": username, "password": password, "host": host, "port": port, "dbname": dbname}
    if username in sessions:
        return sessions[username]()

    engine = create_engine(conn_template % auth_info, echo=echo, pool_pre_ping=pool_pre_ping)
    sessions[username] = sessionmaker(bind=engine)
    return sessions[username]()
