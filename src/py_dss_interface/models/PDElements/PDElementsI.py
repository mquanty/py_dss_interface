# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class PDElementsI(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        int32_t PDElementsI(int32_t Parameter, int32_t Argument);

    This interface returns an integer with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def _count(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(0), ctypes.c_int32(0))

    def _first(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(1), ctypes.c_int32(0))

    def _next(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(2), ctypes.c_int32(0))

    def _is_shunt(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(3), ctypes.c_int32(0))

    def _num_customers(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(4), ctypes.c_int32(0))

    def _total_customers(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(5), ctypes.c_int32(0))

    def _parent_pd_element(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(6), ctypes.c_int32(0))

    def _from_terminal(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(7), ctypes.c_int32(0))

    def _section_id(self) -> int:
        return self._dss_obj.PDElementsI(ctypes.c_int32(8), ctypes.c_int32(0))