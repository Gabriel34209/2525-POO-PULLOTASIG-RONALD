import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple


class TaskManagerApp:
    """
    Aplicación GUI para la gestión de tareas con atajos de teclado.
    """

    # Colores y marcadores
    COLOR_COMPLETED: str = "#d4edda"  # Verde claro para tareas completadas
    COLOR_PENDING: str = "white"  # Blanco para tareas pendientes
    MARKER_COMPLETED: str = "[HECHO] "
    MARKER_PENDING: str = ""

    def __init__(self, master: tk.Tk):
        """Inicializa la aplicación y configura la interfaz."""
        self.master: tk.Tk = master
        self.master.title("Gestión de Tareas Pendientes")
        self.tasks: List[Tuple[str, bool]] = []  # Lista para almacenar tareas: (descripción, completada)

        self._create_widgets()
        self._setup_layout()
        self._bind_keyboard_shortcuts()
        self._load_initial_tasks()  # Opcional: cargar alguna tarea de ejemplo

    def _create_widgets(self):
        """Crea todos los componentes de la interfaz (widgets)."""

        # 1. Campo de entrada para nuevas tareas
        self.entry_task: tk.Entry = tk.Entry(self.master, width=50, font=('Arial', 12))

        # 2. Listbox para mostrar las tareas
        # Se incluye un Scrollbar por si la lista crece mucho
        self.task_list_frame: tk.tk.Frame = tk.Frame(self.master)
        self.task_list_scrollbar: tk.Scrollbar = tk.Scrollbar(self.task_list_frame, orient=tk.VERTICAL)

        self.task_listbox: tk.Listbox = tk.Listbox(
            self.task_list_frame,
            height=15,
            width=50,
            yscrollcommand=self.task_list_scrollbar.set,
            selectmode=tk.SINGLE,  # Permite seleccionar solo una tarea
            font=('Arial', 12)
        )
        self.task_list_scrollbar.config(command=self.task_listbox.yview)

        # 3. Botones de acción
        self.btn_add: tk.Button = tk.Button(self.master, text="Añadir Tarea", command=self.add_task)
        self.btn_complete: tk.Button = tk.Button(self.master, text="Marcar como Hecha (C)", command=self.complete_task)
        self.btn_delete: tk.Button = tk.Button(self.master, text="Eliminar Tarea (D/Del)", command=self.delete_task)

    def _setup_layout(self):
        """Define la disposición de los widgets en la ventana principal."""

        # Layout del campo de entrada y el botón de añadir
        self.entry_task.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
        self.btn_add.grid(row=0, column=1, padx=10, pady=(10, 5))

        # Layout del Listbox y el Scrollbar
        self.task_list_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configurar la expansión de la columna 0 y fila 1 para el listbox
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        # Layout de los botones de acción
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

        self.btn_complete.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.btn_delete.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))

    def _bind_keyboard_shortcuts(self):
        """Asigna los atajos de teclado a las funciones correspondientes."""

        # Atajo: 'Enter' en el campo de entrada para añadir tarea
        self.entry_task.bind('<Return>', lambda event: self.add_task())

        # Atajo: 'C' para completar la tarea seleccionada
        self.master.bind('<c>', lambda event: self.complete_task())
        self.master.bind('<C>', lambda event: self.complete_task())

        # Atajo: 'Delete' o 'D' para eliminar la tarea seleccionada
        self.master.bind('<Delete>', lambda event: self.delete_task())
        self.master.bind('<d>', lambda event: self.delete_task())
        self.master.bind('<D>', lambda event: self.delete_task())

        # Atajo: 'Escape' para cerrar la aplicación
        self.master.bind('<Escape>', lambda event: self.master.quit())

    def _load_initial_tasks(self):
        """Carga algunas tareas iniciales para la demostración."""
        initial_tasks = [
            ("Diseñar la interfaz de Tkinter", True),
            ("Implementar los botones de acción", False),
            ("Configurar los atajos de teclado (Enter, C, D, Escape)", False)
        ]

        for description, is_completed in initial_tasks:
            self.tasks.append((description, is_completed))

        self._update_task_listbox()

    def _update_task_listbox(self):
        """Limpia y rellena el Listbox con las tareas actuales, aplicando el feedback visual."""
        self.task_listbox.delete(0, tk.END)  # Limpiar el Listbox

        for index, (description, is_completed) in enumerate(self.tasks):
            # Determinar el prefijo y color de fondo
            display_text = (self.MARKER_COMPLETED if is_completed else self.MARKER_PENDING) + description
            bg_color = self.COLOR_COMPLETED if is_completed else self.COLOR_PENDING

            # Insertar en el Listbox y configurar el color de fondo
            self.task_listbox.insert(tk.END, display_text)
            self.task_listbox.itemconfig(tk.END, {'bg': bg_color})

    ## --- Funciones de Gestión de Tareas ---

    def add_task(self):
        """Añade una nueva tarea desde el campo de entrada."""
        task_description = self.entry_task.get().strip()

        if task_description:
            # Añadir la tarea como pendiente (False)
            self.tasks.append((task_description, False))
            self._update_task_listbox()
            self.entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una descripción para la tarea.")

    def complete_task(self):
        """Marca la tarea seleccionada como completada (o pendiente)."""
        try:
            # Obtener el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]

            # Obtener y modificar la tupla de tarea
            current_description, is_completed = self.tasks[selected_index]
            new_is_completed = not is_completed  # Alternar el estado

            # Reemplazar la tarea en la lista principal
            self.tasks[selected_index] = (current_description, new_is_completed)

            self._update_task_listbox()
            # Opcional: Re-seleccionar la tarea para mantener el foco
            self.task_listbox.select_set(selected_index)

        except IndexError:
            # No se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar/desmarcar.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            # Obtener el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]

            # Eliminar la tarea de la lista principal
            del self.tasks[selected_index]

            self._update_task_listbox()

        except IndexError:
            # No se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    # Inicialización de la ventana principal de Tkinter
    root = tk.Tk()

    # Crea y ejecuta la aplicación
    app = TaskManagerApp(root)
    root.mainloop()