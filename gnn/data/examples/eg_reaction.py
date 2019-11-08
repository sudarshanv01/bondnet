from gnn.data.database import DatabaseOperation
from gnn.data.reaction import ReactionExtractor
from pprint import pprint


def test_buckets():

    # test get isomer
    db_path = "~/Applications/mongo_db_access/extracted_data/database_LiEC.pkl"
    db = DatabaseOperation.from_file(db_path)
    molecules = db.to_molecules()

    extractor = ReactionExtractor(molecules)
    buckets = extractor.bucket_molecules(keys=["formula", "charge", "spin_multiplicity"])
    pprint(buckets)
    buckets = extractor.bucket_molecules(keys=["formula"])
    pprint(buckets)


def test_extract_A_to_B():
    # db_path = '~/Applications/mongo_db_access/extracted_data/database_LiEC.pkl'
    # db_path = "~/Applications/mongo_db_access/extracted_data/database.pkl"
    db_path = "~/Applications/mongo_db_access/extracted_data/database_n200.pkl"
    db = DatabaseOperation.from_file(db_path)
    molecules = db.to_molecules()
    print("db recovered, number of mols:", len(molecules))

    extractor = ReactionExtractor(molecules)
    extractor.bucket_molecules(keys=["formula", "charge"])
    print("number of buckets", len(extractor.buckets))

    extractor.extract_A_to_B_style_reaction()
    extractor.to_file(
        filename="~/Applications/mongo_db_access/extracted_data/reaction_A2B.pkl"
    )


def test_extract_A_to_B_C():
    # db_path = '~/Applications/mongo_db_access/extracted_data/database_LiEC.pkl'
    # db_path = "~/Applications/mongo_db_access/extracted_data/database.pkl"
    db_path = "~/Applications/mongo_db_access/extracted_data/database_n200.pkl"
    db = DatabaseOperation.from_file(db_path)
    molecules = db.to_molecules()
    print("db recovered, number of moles:", len(molecules))

    extractor = ReactionExtractor(molecules)
    extractor.bucket_molecules(keys=["formula", "charge"])
    print("number of buckets", len(extractor.buckets))

    extractor.extract_A_to_B_C_style_reaction()
    extractor.to_file(
        filename="~/Applications/mongo_db_access/extracted_data/reactions_A2BC.pkl"
    )


def test_extract_one_bond_break():
    # db_path = "~/Applications/mongo_db_access/extracted_data/database.pkl"
    db_path = "~/Applications/mongo_db_access/extracted_data/database_n200.pkl"
    # db_path = "~/Applications/mongo_db_access/extracted_data/database_H.pkl"
    db = DatabaseOperation.from_file(db_path)
    molecules = db.to_molecules()
    print("db recovered, number of moles:", len(molecules))

    extractor = ReactionExtractor(molecules)
    extractor.bucket_molecules(keys=["formula", "charge"])
    print("number of buckets", len(extractor.buckets))

    extractor.extract_one_bond_break()
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions.pkl"
    filename = "~/Applications/mongo_db_access/extracted_data/reactions_n200.pkl"
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions_H.pkl"
    extractor.to_file(filename)


def test_reactants_bond_energies_to_file():
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions.pkl"
    filename = "~/Applications/mongo_db_access/extracted_data/reactions_n200.pkl"
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions_H.pkl"
    extractor = ReactionExtractor.from_file(filename)
    filename = "~/Applications/mongo_db_access/extracted_data/bond_energies_H.yml"
    filename = "~/Applications/mongo_db_access/extracted_data/bond_energies_n200.yml"
    extractor.bond_energies_to_file(filename)


def test_create_struct_label_dataset():
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions_A2B.pkl"
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions_A2BC.pkl"
    # filename = "~/Applications/mongo_db_access/extracted_data/reactions.pkl"
    filename = "~/Applications/mongo_db_access/extracted_data/reactions_n200.pkl"
    extractor = ReactionExtractor.from_file(filename)
    extractor.create_struct_label_dataset(
        struct_name="~/Applications/mongo_db_access/extracted_data/sturct_n200.sdf",
        label_name="~/Applications/mongo_db_access/extracted_data/label_n200.txt",
    )


def test_create_struct_label_dataset_with_lowest_energy_across_charge():
    filename = "~/Applications/mongo_db_access/extracted_data/reactions_n200.pkl"
    extractor = ReactionExtractor.from_file(filename)
    extractor.create_struct_label_dataset_with_lowest_energy_across_charge(
        struct_name="~/Applications/mongo_db_access/extracted_data/sturct_n200.sdf",
        label_name="~/Applications/mongo_db_access/extracted_data/label_n200.txt",
    )


if __name__ == "__main__":
    # test_buckets()
    # test_extract_A_to_B()
    # test_extract_A_to_B_C()
    test_extract_one_bond_break()
    # test_reactants_bond_energies()
    # test_reactants_bond_energies_to_file()
    test_create_struct_label_dataset()
    test_create_struct_label_dataset_with_lowest_energy_across_charge()