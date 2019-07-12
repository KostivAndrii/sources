-- OpenDMARC database schema
--
-- Copyright (c) 2012, The Trusted Domain Project.
--      All rights reserved.

-- A table for mapping domain names and their DMARC policies to IDs

CREATE SCHEMA opendmarc;

CREATE TABLE IF NOT EXISTS opendmarc.domains (
        id SERIAL,
        name VARCHAR(255) NOT NULL,
        firstseen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

        PRIMARY KEY(id),
        UNIQUE (name)
);

-- A table for logging reporting requests
CREATE TABLE IF NOT EXISTS opendmarc.requests (
        id SERIAL,
        domain INT NOT NULL,
        repuri VARCHAR(255),
        adkim SMALLINT,
        aspf SMALLINT,
        policy SMALLINT,
        spolicy SMALLINT,
        pct SMALLINT,
        locked SMALLINT NOT NULL DEFAULT 0,
        firstseen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        lastsent TIMESTAMP DEFAULT NULL,

        PRIMARY KEY(id),
        UNIQUE(domain)
);

-- A table for reporting hosts
CREATE TABLE IF NOT EXISTS opendmarc.reporters (
        id SERIAL,
        name VARCHAR(255) NOT NULL,
        firstseen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

        PRIMARY KEY(id),
        UNIQUE(name)
);

-- A table for IP addresses
CREATE TABLE IF NOT EXISTS opendmarc.ipaddr (
        id SERIAL,
        addr VARCHAR(64) NOT NULL,
        firstseen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

        PRIMARY KEY(id),
        UNIQUE(addr)
);

-- A table for messages
CREATE TABLE IF NOT EXISTS opendmarc.messages (
        id SERIAL,
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        jobid VARCHAR(128) NOT NULL,
        reporter INT NOT NULL,
        policy SMALLINT NOT NULL,
        disp SMALLINT NOT NULL,
        ip INT NOT NULL,
        env_domain INT NOT NULL,
        from_domain INT NOT NULL,
        policy_domain INT NOT NULL DEFAULT 0,
        spf SMALLINT NOT NULL,
        align_dkim SMALLINT NOT NULL,
        align_spf SMALLINT NOT NULL,
        sigcount SMALLINT NOT NULL,

        PRIMARY KEY(id),
        UNIQUE(reporter, date, jobid)
);

-- A table for signatures
CREATE TABLE IF NOT EXISTS opendmarc.signatures (
        id SERIAL,
        message INT NOT NULL,
        domain INT NOT NULL,
        pass SMALLINT NOT NULL,
        error SMALLINT NOT NULL,

        PRIMARY KEY(id),
        UNIQUE(message)
);
