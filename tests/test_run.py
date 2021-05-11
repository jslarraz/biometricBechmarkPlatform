from system import *

eer = {}
for preprocessing in [preprocessing_san18]:
    eer[preprocessing.__name__] = {}

    for feature_extractor in [mean_cycle_san18, multicycles_san18]:
        eer[preprocessing.__name__][feature_extractor.__name__] = {}

        for classifier in [manhattan_san18, euclidean_san18]:
            eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__] = {}

            # System definition
            s = system(preprocessing, feature_extractor, classifier)

            for device in ['nonin', 'berry']:
                eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device] = {}

                for ts in ['d2', 'd3']:
                    eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device][ts] = []

                    for enrollment_gap in [0,5,10]:
                        s.enrollment(from_file('ddbb', device, 'd1', 10+enrollment_gap, 40+enrollment_gap))

                        for testing_gap in [0,5,10]:
                            th, far, frr, eer_aux = s.testing(from_file('ddbb', device, ts, 10+testing_gap, 40+testing_gap))
                            eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device][ts].append(eer_aux)

                    eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device][ts] = mean(eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device][ts])
                    print(mean(eer[preprocessing.__name__][feature_extractor.__name__][classifier.__name__][device][ts]))
print(eer)





