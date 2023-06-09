# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class TransformersI(Base):
    """
    This interface can be used to read/modify the properties of the Transformers Class where the values are integers.

    The structure of the interface is as follows:
        int32_t TransformersI(int32_t Parameter, int32_t argument) ;

    This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of
    the class to be used and the variable “argument” can be used to modify the value of the property when necessary.
    Reading and writing properties are separated and require a different parameter number to be executed.

    The properties (parameter) are integer numbers and are described as follows.
    """

    def _num_windings_read(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(0), ctypes.c_int32(0))

    def _num_windings_write(self, argument) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(1), ctypes.c_int32(argument))

    def _wdg_read(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(2), ctypes.c_int32(0))

    def _wdg_write(self, argument) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(3), ctypes.c_int32(argument))

    def _num_taps_read(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(4), ctypes.c_int32(0))

    def _num_taps_write(self, argument) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(5), ctypes.c_int32(argument))

    def _is_delta_read(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(6), ctypes.c_int32(0))

    def _is_delta_write(self, argument) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(7), ctypes.c_int32(argument))

    def _first(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(8), ctypes.c_int32(0))

    def _next(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(9), ctypes.c_int32(0))

    def _count(self) -> int:
        return self._dss_obj.TransformersI(ctypes.c_int32(10), ctypes.c_int32(0))
