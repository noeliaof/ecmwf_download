import pandas as pd
from datetime import datetime
#
# dictionary of model versions with (start,end)
model_version_specs = dict(
    ECMWF = dict(
        CY43R1 = ('2016-11-22','2017-07-10'),
        CY43R3 = ('2017-07-11','2018-06-05'),
        CY45R1 = ('2018-06-06','2019-06-10'),
        CY46R1 = ('2019-06-11','2020-06-29'),
        CY47R1 = ('2020-06-30','2021-05-10'),
        CY47R2 = ('2021-05-11','2021-10-10'),
        CY47R3 = ('2021-10-11',datetime.strftime(datetime.today(),"%Y-%m-%d"))
    )
)


def which_mv_for_init(fc_init_date,model='ECMWF',fmt='%Y-%m-%d'):
    """
    return model version for a specified initialization date and model
    INPUT:
            fc_init_date:   date string YYYY-mm-dd, datetime.datetime
                            or pandas.Timestamp
            model:          string for the modeling center (currently just
                            'ECMWF' is valid)
                            default: 'ECMWF'
            fmt:            string specifying the date format,
                            default: '%Y-%m-%d'
    OUTPUT:
            model version as string
    """
    if isinstance(fc_init_date,str):
        # convert date string to datetime object:
        fc_init_datetime = pd.Timestamp(fc_init_date)

    elif isinstance(fc_init_date,pd.Timestamp):
        fc_init_datetime = fc_init_date

    elif isinstance(fc_init_date,datetime.datetime):
        fc_init_datetime = pd.Timestamp(fc_init_date)

    else:
        raise TypeError(
            'Input of invalid type was given to date_to_model.which_mv_for_init'
            )

        return None

    # got through the model versions from the above dictionary:
    for MV,mv_dates in model_version_specs[model].items():
        # convert first and last dates to datetime:

        mv_first = pd.Timestamp(mv_dates[0])
        mv_last  = pd.Timestamp(mv_dates[-1])

        # check if the given date is within the current model version's
        # start and end dates:
        if  mv_first <= fc_init_datetime <= mv_last:
            valid_version = MV

    try:
        return valid_version
    except:

        raise ValueError(
            'No matching model version found...'
            )
        return None
