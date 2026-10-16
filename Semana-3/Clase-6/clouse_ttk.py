import ttkbootstrap as tb
from ttkbootstrap.constants import *
from typing import List, Dict, Any, Callable

# ==========================================
# 1. CLOSURES (Estado protegido y configuraciones)
# ==========================================

def crear_calculadora_envio(costo_fijo: float):
    """
    Closure: 'Recuerda' la tarifa de envío del sector.
    No necesitamos pasar la tarifa cada vez que el usuario hace un pedido.
    """
    def calcular(subtotal: float) -> float:
        # Si la compra supera los $20, el envío es gratis
        if subtotal >= 20.0:
            return 0.0
        return costo_fijo
    return calcular


def crear_carrito():
    """
    Closure: Encapsula la lista de productos del pedido.
    Evita que el carrito se pueda borrar o modificar desde fuera sin control.
    """
    items_pedido: List[Dict[str, Any]] = []

    def agregar_producto(producto: Dict[str, Any]):
        items_pedido.append(producto)

    def obtener_pedido():
        return list(items_pedido) # Devolvemos una copia segura

    def limpiar():
        items_pedido.clear()

    return agregar_producto, obtener_pedido, limpiar


# ==========================================
# 2. HOF (Higher-Order Function / Función de Orden Superior)
# ==========================================

def procesar_menu(
    menu: List[Dict[str, Any]], 
    filtro: Callable[[Dict[str, Any]], bool]
) -> List[Dict[str, Any]]:
    """
    HOF: Recibe una función de filtro y la aplica a la lista del menú.
    """
    return list(filter(filtro, menu))


# ==========================================
# 3. INTERFAZ GRÁFICA CON TTKBOOTSTRAP
# ==========================================

class AppRestaurante:
    def __init__(self, root: tb.Window):
        self.root = root
        self.root.title("Pedido Express - Restaurante")
        self.root.geometry("650x700")

        # Menú base de la cocina
        self.menu_disponible = [
            {"id": 1, "nombre": "Hamburguesa Doble", "precio": 8.50, "categoria": "comida"},
            {"id": 2, "nombre": "Pizza Familiar", "precio": 14.00, "categoria": "comida"},
            {"id": 3, "nombre": "Ensalada César", "precio": 6.00, "categoria": "vegetariano"},
            {"id": 4, "nombre": "Jugo Natural", "precio": 2.50, "categoria": "bebida"},
            {"id": 5, "nombre": "Té Helado", "precio": 2.00, "categoria": "bebida"},
        ]

        # Instanciamos los CLOSURES
        self.calcular_envio_centro = crear_calculadora_envio(costo_fijo=2.50)
        self.agregar_al_carrito, self.obtener_carrito, self.limpiar_carrito = crear_carrito()

        self._construir_ui()

    def _construir_ui(self):
        main_frame = tb.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        tb.Label(main_frame, text="🍔 Pedidos de Restaurante", font=("Helvetica", 16, "bold"), bootstyle="primary").pack(anchor="w", pady=(0, 10))

        # --- SECCIÓN 1: FILTRO DE MENÚ (HOF + Lambdas) ---
        frame_filtros = tb.LabelFrame(main_frame, text=" Filtrar Menú (HOF) ", padding=10)
        frame_filtros.pack(fill=X, pady=(0, 10))

        # Botones que pasan LAMBDAS a la HOF 'procesar_menu'
        tb.Button(
            frame_filtros, text="Todos", bootstyle="outline-primary",
            command=lambda: self.mostrar_menu(lambda item: True)
        ).pack(side=LEFT, padx=5)

        tb.Button(
            frame_filtros, text="Solo Bebidas", bootstyle="outline-info",
            command=lambda: self.mostrar_menu(lambda item: item["categoria"] == "bebida")
        ).pack(side=LEFT, padx=5)

        tb.Button(
            frame_filtros, text="Económicos (< $8)", bootstyle="outline-success",
            command=lambda: self.mostrar_menu(lambda item: item["precio"] < 8.0)
        ).pack(side=LEFT, padx=5)

        # --- SECCIÓN 2: LISTA DEL MENÚ ---
        self.lista_menu = tb.Treeview(main_frame, columns=("nombre", "precio"), show="headings", height=5)
        self.lista_menu.heading("nombre", text="Plato / Bebida")
        self.lista_menu.heading("precio", text="Precio")
        self.lista_menu.pack(fill=X, pady=(0, 10))

        # Botón para agregar el ítem seleccionado
        tb.Button(main_frame, text="➕ Agregar Seleccionado al Carrito", bootstyle="primary", command=self.agregar_item).pack(anchor="w", pady=(0, 15))

        # --- SECCIÓN 3: RESUMEN DEL PEDIDO (CLOSURE) ---
        frame_resumen = tb.LabelFrame(main_frame, text=" Resumen de la Orden (Closure) ", padding=10)
        frame_resumen.pack(fill=BOTH, expand=True)

        # Lista para ver los productos que se están comprando
        self.lista_carrito = tb.Treeview(frame_resumen, columns=("producto", "precio"), show="headings", height=5)
        self.lista_carrito.heading("producto", text="Producto en la Orden")
        self.lista_carrito.heading("precio", text="Precio")
        self.lista_carrito.pack(fill=BOTH, expand=True, pady=(0, 10))

        frame_totales_acciones = tb.Frame(frame_resumen)
        frame_totales_acciones.pack(fill=X)

        frame_totales = tb.Frame(frame_totales_acciones)
        frame_totales.pack(side=LEFT, fill=X, expand=True)

        self.lbl_items = tb.Label(frame_totales, text="Productos en carrito: 0", font=("Helvetica", 10))
        self.lbl_items.pack(anchor="w")

        self.lbl_subtotal = tb.Label(frame_totales, text="Subtotal: $0.00", font=("Helvetica", 10))
        self.lbl_subtotal.pack(anchor="w")

        self.lbl_envio = tb.Label(frame_totales, text="Envío: $0.00", font=("Helvetica", 10))
        self.lbl_envio.pack(anchor="w")

        self.lbl_total = tb.Label(frame_totales, text="Total: $0.00", font=("Helvetica", 11, "bold"), bootstyle="success")
        self.lbl_total.pack(anchor="w", pady=(5, 0))

        # Botón para vaciar el carrito aprovechando el closure limpiar_carrito
        tb.Button(
            frame_totales_acciones,
            text="🗑️ Vaciar Carrito",
            bootstyle="outline-danger",
            command=self.vaciar_item_carrito
        ).pack(side=RIGHT, anchor="s")

        # Cargar menú completo al iniciar
        self.mostrar_menu(lambda item: True)

    def mostrar_menu(self, criterio_filtro: Callable):
        """Usa la HOF procesar_menu pasándole una lambda"""
        for row in self.lista_menu.get_children():
            self.lista_menu.delete(row)

        # Aplicamos la HOF
        menu_filtrado = procesar_menu(self.menu_disponible, criterio_filtro)

        for item in menu_filtrado:
            self.lista_menu.insert("", END, values=(item["nombre"], f"${item['precio']:.2f}"))

    def actualizar_vista_carrito(self):
        """Actualiza la tabla del carrito y los totales usando los Closures"""
        pedido_actual = self.obtener_carrito()

        # Limpiar y repoblar la lista de productos que se están comprando
        for row in self.lista_carrito.get_children():
            self.lista_carrito.delete(row)

        for item in pedido_actual:
            self.lista_carrito.insert("", END, values=(item["nombre"], f"${item['precio']:.2f}"))

        # Usamos una Lambda en línea para sumar precios rápidamente
        subtotal = sum(map(lambda p: p["precio"], pedido_actual))
        
        # Uso del Closure de costo de envío
        envio = self.calcular_envio_centro(subtotal) if pedido_actual else 0.0
        total = subtotal + envio

        # Renderizar en la interfaz
        self.lbl_items.config(text=f"Productos en carrito: {len(pedido_actual)}")
        self.lbl_subtotal.config(text=f"Subtotal: ${subtotal:.2f}")
        self.lbl_envio.config(text=f"Envío (Gratis > $20): ${envio:.2f}")
        self.lbl_total.config(text=f"Total Final: ${total:.2f}")

    def agregar_item(self):
        seleccion = self.lista_menu.selection()
        if not seleccion:
            return

        # Obtener datos de la fila seleccionada
        item_vals = self.lista_menu.item(seleccion[0])["values"]
        nombre = item_vals[0]
        precio = float(str(item_vals[1]).replace("$", ""))

        # 1. Uso del Closure: Agregamos al carrito privado
        self.agregar_al_carrito({"nombre": nombre, "precio": precio})

        # 2. Actualizamos la vista consultando el Closure
        self.actualizar_vista_carrito()

    def vaciar_item_carrito(self):
        # 1. Uso del Closure: Limpiamos el carrito privado
        self.limpiar_carrito()

        # 2. Actualizamos la vista consultando el Closure
        self.actualizar_vista_carrito()


if __name__ == "__main__":
    app_root = tb.Window(themename="flatly")
    app = AppRestaurante(app_root)
    app_root.mainloop()