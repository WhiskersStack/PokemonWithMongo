import boto3
import json


def update_dynamo_db():
    dynamodb = boto3.resource("dynamodb", region_name='us-west-2')

    with open("data/pokemon_list.json") as f:
        pokemons = json.load(f)

    table = dynamodb.Table("Pokemon")

    with table.batch_writer() as batch:
        for p in pokemons:
            batch.put_item(Item=p)      # must include id & name keys

    print(f"DynamoDB table 'Pokemon' updated with {len(pokemons)} items.")


if __name__ == "__main__":
    update_dynamo_db()
    print("DynamoDB updated successfully.")
