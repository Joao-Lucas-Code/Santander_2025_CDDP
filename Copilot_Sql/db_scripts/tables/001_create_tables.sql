CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collections_set_name VARCHAR(255) NOT NULL,
    release_date DATE,
    total_cards_in_collection INTEGER
);

CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stage_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES tbl_collections(id) ON DELETE CASCADE,
    type_id INTEGER REFERENCES tbl_types(id),
    stage_id INTEGER REFERENCES tbl_stages(id),
    name VARCHAR(50) NOT NULL,
    hp INTEGER,
    attack VARCHAR(50),
    damage VARCHAR(50),
    weakness VARCHAR(50),
    resistance VARCHAR(50),
    retreat_cost INTEGER,
    card_number_in_collection INTEGER
);