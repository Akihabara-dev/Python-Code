# English
# This method returns the main IP of the local machine, that is, the default route.
# We can also use this function to create a user-defined function that doesn't need any routable internet access.

# Spanish
# Este método devuelve la IP principal de la máquina local, es decir, la ruta por defecto.
# También podemos usar esta función para crear una función definida por el usuario que no necesita ningún acceso a Internet enrutable.
import socket
def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
print(extract_ip())