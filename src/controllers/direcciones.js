import { usuarioModel } from "../models/usuarios.js";
import { direccionRequestDTO } from "../dtos/direcciones.js";

export const crearDireccion = async (req, res) => {
  try {
    console.log(req.user);
    const data = direccionRequestDTO(req.body);
    req.user.direcciones.push(data);
    await req.user.save(); // sirve para guardar los cambios realizados de una instancia de cualquier collection de la bd

    return res.status(201).json({
      message: "Direccion agregada exitosamente",
      result: req.user.direcciones,
    });
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    });
  }
};

export const listarDirecciones = async (req, res) => {
  return res.json({
    message: null,
    result: req.user.direcciones,
  });
};


export const modificarDireccion = async(req, res) =>{
  try {
    const data = direccionRequestDTO(req.body);
    const result = req.user.direcciones.id(req.params.id)
    result.set(data);
    await req.user.save();
    return res.json({
      message: 'La dirección se actualizo correctamente',
      result
    })
    
  } catch (error) {
    return res.status(400).json({
      message: 'Error al actualizar la dirección',
      result: error.message
    })
  }

}

export const borrarDireccion = async(req, res) =>{
  try {
    
    req.user.direcciones.id(req.params.id).remove();
    req.user.save();

    return res.json({
      message: 'La dirección se elimino correctamente',
      result: null
    })
    
  } catch (error) {
    return res.status(400).json({
      message: 'Error al eliminar la dirección',
      result: error.message
    })
  }

}