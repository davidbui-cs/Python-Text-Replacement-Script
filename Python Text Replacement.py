import os


HTML_FILE ='map_month_range_1.html'
file_data = ''
JS_folder_name = 'Javascript/'
CSS_folder_name = 'CSS/'

#JAVASCRIPT REPLACEMENT DICTIONARY
#KEY: What you want to replace.
#VALUE: What you want to replace the key with.
JS_replacements = {
                'https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js':
                                'Leaflet 1.5.1.js',
                
                'https://code.jquery.com/jquery-1.12.4.min.js':
                                'jquery-1.12.4.min.js',
                
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js':
                                'bootstrap.min.js',
                
                'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js':
                                'leaflet.awesome-markers.js',
                
                'https://rawcdn.githack.com/nezasa/iso8601-js-period/master/iso8601.min.js':
                                'iso8601.min.js',
                
                'https://rawcdn.githack.com/socib/Leaflet.TimeDimension/master/dist/leaflet.timedimension.min.js':
                                'leaflet.timedimension.min.js',
                
                'https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/pa7_hm.min.js':
                                'pa7_hm.min.js',
                
                'https://rawcdn.githack.com/pa7/heatmap.js/develop/plugins/leaflet-heatmap/leaflet-heatmap.js':
                                'leaflet-heatmap.js'
                }


#CSS REPLACEMENT DICTIONARY
#FORMAT:
#{KEY: VALUE, ...}
#KEY: What you want to replace.
#VALUE: What you want to replace the key with.
CSS_replacements = {'https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css':
                                'leaflet.css',
                    
                    'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css':
                                'bootstrap.min.css',
                    
                    'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css':
                                'bootstrap-theme.min.css',
                    
                    'https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css':
                                'font-awesome.min.css',
                    
                    'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css':
                                'leaflet.awesome-markers.css',
                    
                    'https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css':
                                'leaflet.awesome.rotate.css',
                    
                    'Leaflet.TimeDimension.css':
                                'Leaflet.TimeDimension.css'
                    }

                
def load_HTML():
    global file_data
    global HTML_FILE
    
    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(base, HTML_FILE))
    file_data = html.read()

    
def replace_contents():
    global file_data
    global JS_folder_name
    global CSS_folder_name
    
    for key, value in JS_replacements.items():
        file_data = file_data.replace(key, JS_folder_name + value)
    
    for key, value in CSS_replacements.items():
        file_data = file_data.replace(key, CSS_folder_name + value)                     
    

def write_contents():
    global HTML_FILE
    
    with open(HTML_FILE, "w") as f_output:
        f_output.write(file_data)



if __name__ == "__main__":
    load_HTML()
    replace_contents()
    write_contents()
