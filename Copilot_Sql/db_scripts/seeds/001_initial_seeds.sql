INSERT INTO tbl_collections (collections_set_name, release_date, total_cards_in_collection) 
VALUES ('Scarlet & Violet: 151', '2023-09-22', 165);

INSERT INTO tbl_types (type_name) VALUES 
('Fire'), ('Water'), ('Grass'), ('Lightning'), ('Psychic'), 
('Fighting'), ('Darkness'), ('Metal'), ('Colorless'), ('Dragon');

INSERT INTO tbl_stages (stage_name) VALUES 
('Basic'), ('Stage 1'), ('Stage 2'), ('VMAX'), ('VSTAR'), ('ex');

INSERT INTO tbl_cards (
    collection_id, 
    type_id, 
    stage_id, 
    name, 
    hp, 
    attack, 
    damage, 
    weakness, 
    resistance, 
    retreat_cost, 
    card_number_in_collection
) VALUES (
    (SELECT id FROM tbl_collections WHERE collections_set_name = 'Scarlet & Violet: 151'),
    (SELECT id FROM tbl_types WHERE type_name = 'Fire'),
    (SELECT id FROM tbl_stages WHERE stage_name = 'Stage 2'),
    'Charizard ex',
    330,
    'Explosive Vortex',
    '330',
    'Water x2',
    'None',
    2,
    183
);