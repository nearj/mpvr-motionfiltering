# coding: utf-8
from mpvr.utils.process import *

def main():
    from mpvr.datamanager.threedi import ThreeDI as dm

    dm = dm.from_config()
    for scenario in dm.get_scenarios():
        print(scenario)
        dm.set_scenario(scenario)
        histograms = make_histogram(dm.load(), (5**6, 36))
        mp_entropy = [x for x in to_mp_entropy(mapping_src_to_histogram(dm.load(), histograms))]
        # entropy = [x for x in to_entropy(
        #     [x[1] for x in mapping_src_to_histogram(dm.load(), histograms)])]

        # dm.save_as_table(entropy, 'ent')
        dm.save_as_table(mp_entropy, 'mpe')
        # dm.save_as_graph(entropy, 'ent', ylim=[0, 300000])
        dm.save_as_graph(mp_entropy, 'mpe', ylim=[-300000, 300000])


if __name__ == '__main__':
    main()


from mpvr.datamanager.threedi import ThreeDI as dm
from mpvr.utils.process import *

dm = dm.from_config()
holder = {}
for scenario in dm.get_scenarios():
    dm.set_scenario(scenario)
    mpe = dm._load_processed_data('mpe')[1]
    incidence = dm._load_incidence()
    holder[scenario] = correlation(mpe, incidence)
dm._save_correaltion_as_table(holder, 'mpe')
