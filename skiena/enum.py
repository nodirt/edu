def enum(typeName, *sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type(typeName, (), enums)