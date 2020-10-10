from .models import DHT11
from graphql import GraphQLError


def resolver_dht11s():
    try:
        return DHT11.objects.all()
    except DHT11.DoesNotExist:
        raise GraphQLError(
            "Could not find any DHT11 object ")


def resolver_dht11est():
    try:
        return DHT11.objects.latest('timestamp')
    except DHT11.DoesNotExist:
        raise GraphQLError(
            "Could not find the DHT11 object with Latest ! ")


def resolver_create_dht11(temperature, humidity):
    return DHT11.objects.create(
        temperature=temperature,
        humidity=humidity
    )


def resolver_update_dht11(id, timestamp, temperature, humidity):
    _ = DHT11.objects.get(id=id).delete()
    return DHT11.objects.create(
        id=id,
        timestamp=timestamp,
        temperature=temperature,
        humidity=humidity
    )


def resolver_delete_dht11(id):
    try:
        _ = DHT11.objects.get(id=id).delete()
    except DHT11.DoesNotExist:
        raise GraphQLError(
            "Could not find the DHT11 object with given id: " + str(id))
