from highcharts import Highchart
chart = Highchart()

options = {
    'chart': {
        'type': 'line',
        'zoomType': 'xy'
    },

    'title': {
        'text': 'Highchart Line'
    },

    'legend': {
        'enabled': True
    },
        
    'xAxis': {
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'title': {
            'text': 'Months of the year'}
    },
    
    'yAxis': {
        'title': {
            'text': 'Number of followers'
        }
    },
}

data1 = [7, 7, 9, 14, 18, 21, 25, 26, 30, 55, 62, 85]
data2 = [11, 17, 22, 25, 56, 76, 91, 102, 150]
data3 = [3, 4, 5, 8, 11, 15, 17, 36, 42, 103, 126, 148]

chart.set_dict_options(options)
chart.add_data_set(data1, 'line', 'User 1')
chart.add_data_set(data2, 'line', 'User 2')
chart.add_data_set(data3, 'line', 'User 3')

chart.save_file('./line-highcharts')