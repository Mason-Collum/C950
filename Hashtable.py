class Hashtable:
    def __init__(self, capactity_initial=40):
        self.table = []
        for i in range(capactity_initial):
            self.table.append([])

    def insert(self, key, item, ):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for ki in bucket_list:
            if ki[0] == key:
                ki[1] = item
                return True

        value_key = [key, item]
        bucket_list.append(value_key)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for k in bucket_list:
            if k[0] == key:
                return k[1]

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
