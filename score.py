import json


class Score:
    """
    Define a score with filename
    """

    def __init__(self, filename):
        """
        initialize new score
        :param filename: string
        """
        self.filename = filename

    def insert(self, name, stage, score):
        """
        insert new score and stage with player name to user_data.json
        :param name: Player name(string)
        :param stage: int
        :param score: int
        """
        new_data = {
            name: {'stage': stage,
                   "score": score}
        }
        try:
            with open(f"{self.filename}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{self.filename}.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            try:
                if score >= data[name]["score"] or stage > data[name]["stage"]:
                    data.update(new_data)
                    with open(f"{self.filename}.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
            except KeyError:
                data.update(new_data)
                with open(f"{self.filename}.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

    def score_display(self):
        """
        display score board in terminal and sort by stage player get
        """
        with open(self.filename, "r") as data_file:
            data = json.load(data_file)
            stage = []
            stage_list = []
            for value in data.values():
                if value['stage'] not in stage:
                    stage.append(value['stage'])
            st_stage = sorted(stage, reverse=True)
            count = 1
            print(
                '=====| Score |=============================================')
            if not stage:
                print('no one have play the game')
            else:
                for i in st_stage:
                    for k, v in data.items():
                        if v['stage'] == i:
                            stage_list.append({k: v})
                            print(
                                f'{count}) Name: {k} ,arrive floor: '
                                f'{v["stage"]} time: {int(v["score"])}')
                            count += 1
