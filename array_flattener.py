import json
import argparse


class ArrayFlattener(object):
    def __init__(self, nested_array):
        """
        Instantiate with nested array, call .process and then .get_result()
        :param nested_array:
        :return: flat array
        """
        self.flat_array = []
        self.nested_array = nested_array

    def process(self):
        self.flat_array = list(self.__flattener(self.nested_array))
        return self

    def get_result(self, result_type='list'):
        """
        get results in your preferred type
        :param result_type: define the expected out put type 'list','json' by default it is obj
        :return:
        """
        result_factory = {
            'json': json.dumps(self.flat_array),
            'list': self.flat_array,
        }
        return result_factory[result_type]

    def __flattener(self, list):
        for elm in list:
            try:
                for _elm in self.__flattener(elm):
                    yield _elm
            except:
                yield elm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--array', help='<Required> array in json type', required=True, dest='array', type=json.loads)
    args = parser.parse_args()
    array_flattener = ArrayFlattener(args.array)
    array_flattener.process()
    print(array_flattener.get_result())