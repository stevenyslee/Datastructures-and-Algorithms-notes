//
// Created by Stelios on 05/01/2018.
//

#ifndef DS_AL_COMMON_H
#define DS_AL_COMMON_H

#include <errno.h>
#include <assert.h>

#define insert(_ptr, type, element)                                             \
    do{                                                                         \
        assert(_ptr);                                                           \
        assert(element);                                                        \
        insert_##type(_ptr, element);                                           \
    }while(0);

#define remove_el(strct, type, element,comp)                                    \
    do{                                                                         \
        assert(_ptr);                                                           \
        assert(comp);                                                           \
        remove_##type(strct, element, comp)                                     \
    }

#define find(strct, type, element,comp) find_##type(strct, element, comp)

#define destroy(_ptr,type,del_elem)                                                      \
    do{                                                                         \
        assert(_ptr);                                                           \
        destroy_##type(_ptr,1,del_elem);                                                 \
}while(0)

#define destroy_arr(_ptr,type,count)                                            \
    do{                                                                         \
        assert((count)>=0);                                                     \
        assert(_ptr);                                                           \
        destroy_##type(_ptr,count);                                             \
    }while(0)

#define _new(_ptr, type)                                                        \
    do{                                                                         \
        _ptr = malloc(sizeof(type));                                          \
        if (!(_ptr)) return ENOMEM;                                             \
            create_##type(_ptr, 1);                                             \
    }while(0)

#define _new_a(_ptr, type, count)                                               \
    do{                                                                         \
        assert((count)>=1);                                                     \
        (_ptr) = malloc(sizeof(type)*(count));                                  \
        if (!(_ptr)) return ENOMEM;                                             \
            create_##type(_ptr, (count));                                       \
    }while(0)

#endif //DS_AL_COMMON_H
