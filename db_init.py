from sqlalchemy.orm import sessionmaker
from connect_connector import engine

from data_model import Package

def create_packages():
    # Create a session
    session = sessionmaker(bind=engine)()

    # Create 10 sample packages
    for i in range(10):
        package = Package(
            product_id=i,
            height=10.0 + i,
            width=10.0 + i ,
            depth=10.0 + i,
            weight=10.0 + i,
            special_handling_instructions="No special handling instructions for package" + str(i)
        )

        # Add the package to the session
        session.add(package)

    # Commit the changes
    session.commit()

if __name__ == '__main__':
    create_packages()

    print('Packages created successfully.')
